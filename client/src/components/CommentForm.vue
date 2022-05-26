<template>
  <form
    @submit.prevent="onSubmit"
    class="comment-list-form">
    <input type="text" id="comment" v-model="content" placeholder="Type comment..." required autofocus>
    <button class="btn"><i class="fa-solid fa-paper-plane"></i></button>
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

<style>
</style>