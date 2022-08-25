<template>
  <div>
    <ul class="comments p-0 mt-2 mb-1">
      <comment-list-item
        v-for="(comment, idx) in commentSet"
        :key="comment.id"
        :comment="comment"
        :isMaxIdx="idx === commentSet.length - 1"
        @update-comment="onUpdate"
        @delete-comment="onDelete"
      >
      </comment-list-item>
    </ul>

    <comment-form @create-comment="onCreate"></comment-form>
  </div>
</template>

<script>
import CommentListItem from "@/components/CommentListItem.vue";
import CommentForm from "@/components/CommentForm.vue";

import drf from "@/api/drf";
import axios from "axios";
import { mapGetters } from "vuex";

export default {
  name: "CommentList",

  data() {
    return {
      commentSet: this.comments,
    };
  },

  components: {
    CommentForm,
    CommentListItem,
  },

  props: {
    review: Object,
    comments: Array,
  },

  computed: {
    ...mapGetters(["authHeader"]),
  },

  methods: {
    createComment({ reviewPk, content }) {
      const comment = { content };
      axios({
        url: drf.community.createComment(reviewPk),
        method: "post",
        data: comment,
        headers: this.authHeader,
      })
        .then((res) => {
          this.commentSet.push(res.data);
          this.$emit("comment-emit", this.review.id, this.commentSet);
        })
        .catch((err) => console.error(err.response));
    },

    updateComment({ reviewPk, commentPk, content }) {
      const comment = { content };

      axios({
        url: drf.community.comment(reviewPk, commentPk),
        method: "put",
        data: comment,
        headers: this.authHeader,
      })
        .then((res) => {
          this.commentSet = this.commentSet.map((comment) => {
            if (comment.id === res.data.id) {
              comment = res.data;
            }
            return comment;
          });

          this.$emit("comment-emit", this.review.id, this.commentSet);
        })
        .catch((err) => console.error(err.response));
    },

    deleteComment({ reviewPk, commentPk }) {
      if (confirm("삭제하시겠습니까?")) {
        axios({
          url: drf.community.comment(reviewPk, commentPk),
          method: "delete",
          headers: this.authHeader,
        })
          .then(() => {
            this.commentSet = this.commentSet.filter((comment) => {
              return comment.id !== commentPk;
            });

            this.$emit("comment-emit", this.review.id, this.commentSet);
          })
          .catch((err) => console.error(err.response));
      }
    },

    onCreate(content) {
      this.createComment({
        reviewPk: this.review.id,
        content: content,
      });
    },

    onUpdate(payload) {
      this.updateComment(payload);
    },

    onDelete(payload) {
      this.deleteComment(payload);
    },
  },
};
</script>

<style scoped>
.comments {
  border-radius: 8px;
  width: 100%;
  height: 5rem;
  overflow: auto;
}

.comments::-webkit-scrollbar {
  width: 10px;
}

.comments::-webkit-scrollbar-thumb {
  background-color: #555;
  border-radius: 10px;
  background-clip: padding-box;
  border: 2px solid transparent;
}

.comments::-webkit-scrollbar-track {
  border-radius: 10px;
}
</style>
