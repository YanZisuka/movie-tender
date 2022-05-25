<template>

<form @submit.prevent="onSubmit">
  <div>
      <label for="movie">movie : </label>
      <input v-model="newReview.movie" type="text" id="movie" />
  </div>
  <div>
    <label for="content">content : </label>
    <input v-model="newReview.content" type="text" id="content" />
  </div>
  <div>
    <button>{{ action }}</button>
  </div>
</form>

</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'ReviewForm',
  props: {
    review : Object,
    action : String,
  },
  data() {
    return {
      newReview: {
        movie : this.review.movie,
        content: this.review.content,
      }
    }
  },
  methods : {
    ...mapActions(['createReview', 'updateReview']),
    onSubmit(){
      if (this.action === 'create'){
        this.createReview(this.newReview)
      } else if (this.action === 'update'){
        const payload = {pk: this.review.id,
            ...this.newReview,
          }
          this.updateReview(payload)
      }
    },
  },

}
</script>

<style>

</style>