<template>
  <li>
     <router-link :to="{ name: 'profile', params: { username: comment.user } }">
      {{ comment.user }}
    </router-link>: 
    
    <span v-if="!isEditing">{{ payload.content }}</span>
    <span v-if="isEditing">
      <p>
      <input type="text" v-model="payload.content">
      </p>
      <button @click="onUpdate">Update</button> |
      <button @click="switchIsEditing">Cancle</button>
    </span>

    <span v-if="currentUser.pk === comment.user && !isEditing">
      <button @click="switchIsEditing">Edit</button> |
      <button @click="deleteComment(payload)">Delete</button>
    </span>
    <hr>
  </li>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListItem',
  props: { comment: Object },
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
    ...mapActions(['updateComment', 'deleteComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateComment(this.payload)
      this.isEditing = false
    }
  },

}
</script>

<style>

</style>