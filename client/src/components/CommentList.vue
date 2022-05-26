<template>
  <div class="mb-4">
    
    <ul class="p-0">
      <comment-list-item 
        v-for="comment in comment_set" 
        :key="comment.id"
        :comment="comment"
        @update-comment="updateEmit"
        @delete-comment="deleteEmit"
        >
      </comment-list-item>        
    </ul>

    <comment-form
    @create-comment="createEmit"
    ></comment-form>

  </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem.vue'
import CommentForm from '@/components/CommentForm.vue'

import drf from '@/api/drf'
import axios from 'axios'
import { mapGetters } from 'vuex'

export default {
  name: 'CommentList',

  data() {
    return {
      comment_set: this.comments,
    }
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
    ...mapGetters(['authHeader'])
  },

  methods: {
    createComment({ reviewPk, content }) {
      const comment = { content }
      axios({
        url: drf.community.createComment(reviewPk),
        method: 'post',
        data: comment,
        headers: this.authHeader,
      })
        .then(res => {
          this.comment_set.push(res.data)
        })
        .catch(err => console.error(err.response))
    },

    updateComment({ reviewPk, commentPk, content }) {
      const comment = { content }

      axios({
        url: drf.community.comment(reviewPk, commentPk),
        method: 'put',
        data: comment,
        headers: this.authHeader,
      })
        .then(res => {
          console.log(res.data)
          this.comment_set.forEach(comment => {
            if (comment.id === res.data.id) {
              comment = res.data
            }
          })
        })
        .catch(err => console.error(err.response))
    },

    deleteComment({ reviewPk, commentPk }) {

      if (confirm('삭제하시겠습니까?')) {
        axios({
          url: drf.community.comment(reviewPk, commentPk),
          method: 'delete',
          data : {},
          headers: this.authHeader,
        })
          .then(res => {
            console.log(res.data)
            this.comment_set = this.comment_set.filter(comment => {
              if (comment.id !== commentPk) {
                return true
              }
            })
          })
          .catch(err => console.error(err.response))
      }
    },
    
    createEmit(content) {
      this.createComment({ reviewPk: this.review.id, content: content})
    },

    updateEmit(payload) {
      this.updateComment(payload)
    },

    deleteEmit(payload) {
      this.deleteComment(payload)
    },
  },
}
</script>

<style>
</style>