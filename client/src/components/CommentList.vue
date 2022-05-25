<template>
  <div>
    
    <comment-form></comment-form>
    <ul>
      <comment-list-item 
        v-for="comment in comments" 
        :comment="comment" 
        :key="comment.id">
      </comment-list-item>        
    </ul>

  </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem.vue'
import CommentForm from '@/components/CommentForm.vue'


export default {
  name: 'CommentList',
  components: { CommentForm, CommentListItem },
  props: { comments: Array },
}
</script>

<style>
</style>