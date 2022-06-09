<template>
  <form
    @submit.prevent="onSubmit"
    class="comment-list-form d-flex justify-content-between">
    <input type="text" id="comment" v-model="content" placeholder="댓글 작성" required>
    <button class="btn btn-sm"><i class="fa-solid fa-paper-plane"></i></button>
  </form>
</template>

<script>

export default {
  name: 'CommentForm',

  data() {
    return {
      content: ''
    }
  },

  props: {},

  computed: {},

  methods: {
    onSubmit() {
      this.$emit('create-comment', this.content)
      this.content = ''
    },
  },
}
</script>

<style scoped>
.comment-list-form {
  background-color: #eee;
  width: 98.3%;
  border-radius: 8px;
}

.comment-list-form input {
  background-color: #eee;
  width: 100%;
  border: 0;
  border-radius: 8px;
  padding: 0 1rem;
}
</style>