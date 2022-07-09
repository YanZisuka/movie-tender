<template>
  <li :class="isMaxIdx ? '' : 'mb-4'" class="comment-list d-flex justify-content-between">

    <div>
      <router-link class="fw-bold" :to="{ name: 'profile', params: { username: comment.user.username } }">
        {{ comment.user.nickname }}
      </router-link>

      <br>

      <span v-if="!isEditing">{{ comment.content }}</span>
      <input v-if="currentUser.pk === comment.user.id && isEditing" type="text" v-model="payload.content">
    </div>

    <div>
      <div v-if="currentUser.pk === comment.user.id && !isEditing">
        <button class="btn btn-sm" @click="switchIsEditing"><i class="fa-solid fa-pen"></i></button>
        <button class="btn btn-sm" @click="onDelete"><i class="fa-solid fa-delete-left"></i></button>
      </div>

      <div v-if="currentUser.pk === comment.user.id && isEditing">
        <button class="btn btn-sm" @click="onUpdate"><i class="fa-solid fa-pen"></i></button>
        <button class="btn btn-sm" @click="switchIsEditing"><i class="fa-solid fa-arrow-left-long"></i></button>
      </div>
    </div>
    

  </li>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'CommentListItem',

  props: {
    comment: Object,
    isMaxIdx: Boolean,
  },

  data() {
    return {
      isEditing: false,
      payload: {
        reviewPk: this.comment.review,
        commentPk: this.comment.id,
        content: this.comment.content,
      },
    }
  },

  computed: {
    ...mapGetters(['currentUser']),
  },

  methods: {
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },

    onUpdate() {
      this.$emit('update-comment', this.payload)
      this.isEditing = false
    },

    onDelete() {
      this.$emit('delete-comment', this.payload)
    }
  },
}
</script>

<style scoped>
.comment-list {
  list-style: none;
  padding: 0.7rem 1rem 1rem 1rem;
  background-color: var(--adaptiveGrey100);
  border-radius: 8px;
}

.comment-list a {
  text-decoration: none;
  color: var(--black);
}

.comment-list a:hover {
  color: var(--adaptiveGrey800);
}
</style>