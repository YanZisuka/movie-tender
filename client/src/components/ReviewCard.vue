<template>
  <div >
    <router-link 
    :to="{ name: 'reviewDetail', params: { reviewPk: review.id} }">
    <div class="card">
      <div class="card-body">
        <!-- <img src="{{ review.posterPath }}" class="card-img-top" alt="..."> -->
        <h5 class="card-title mt-2">{{ review.content }}</h5>
        <!-- <p class="card-text">{{ review.overview}}</p> -->
      </div>
    </div>
    </router-link>
  </div>
</template>
<script>
export default {
  name: "ReviewCard",
  props: {
    review : Object,
  },
  computed : {},
}
</script>

<style>

</style>