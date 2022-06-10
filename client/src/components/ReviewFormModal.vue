<template>
  <div class="form-body text-start pt-3 pb-5 px-5">

    <h1 class="text-fff">리뷰쓰기</h1>

    <form @submit.prevent="createReview(payload)" class="d-flex flex-column">
      <label for="content" class="text-fff">내용</label>
      <textarea v-model="payload.content" id="content" cols="30" rows="10" required></textarea>
      <button class="btn-theme align-self-center mt-5">작성</button>
    </form>

  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'ReviewFormModal',

  props: {
    movieDetail: Object,
  },

  data() {
    return {
      payload: {
        movie: this.movieDetail.id,
        content: '',
      },
    }
  },

  methods: {
    ...mapActions(['createReview',])
  },

}
</script>

<style scoped>
.form-body h1 {
  font-weight: 700;
  margin: 0 0 3rem 0;
}

.form-body label {
  font-weight: 700;
  margin: 0 0 3px 0;
}

.form-body textarea {
  width: 100%;
  border: 2px solid #ddd;
  border-radius: 8px;
  padding: 0 1rem;
  margin: 0 0 2rem 0;
}

textarea::-webkit-scrollbar {
  width: 10px;
}

textarea::-webkit-scrollbar-thumb {
  background-color: #555;
  border-radius: 10px;
  background-clip: padding-box;
  border: 2px solid transparent;
}

textarea::-webkit-scrollbar-track {
  border-radius: 10px;
}
</style>