<template>
  <li class="comment-list">
    <router-link class="" :to="{ name: 'profile', params: { username: comment.user.username } }">
      {{ comment.user.nickname }}
    </router-link>: 
    
    <span v-if="!isEditing">{{ payload.content }}</span>
    <span v-if="isEditing">
      <p>
      <input type="text" v-model="payload.content">
      </p>
      <button class="btn" @click="onUpdate"><i class="fa-solid fa-pen"></i></button> |
      <button class="btn" @click="switchIsEditing"><i class="fa-solid fa-arrow-left-long"></i></button>
    </span>

    <span v-if="currentUser.pk === comment.user.id && !isEditing">
      <button class="btn" @click="switchIsEditing"><i class="fa-solid fa-pen"></i></button> |
      <button class="btn" @click="onDelete"><i class="fa-solid fa-xmark"></i></button>
    </span>
  </li>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'CommentListItem',

  props: {
    comment: Object,
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

<style>
.comment-list {
  list-style: none;
}

.comment-list > a {
  text-decoration: none;
  color: #000;
}

.comment-list > a:hover {
  color: #c4c4c4;
}
</style>