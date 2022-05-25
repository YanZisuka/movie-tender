<template>
  <div>

  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'MovieDetailView',

  data() {
    return {}
  },

  computed: {
    ...mapGetters(['currentUser', 'movieDisplayCard'])
  },

  methods: {
    ...mapActions(['fetchCurrentUser', 'fetchMovieDisplayCard'])
  },

  created() {
    this.fetchCurrentUser()
  },
}
</script>

<style>

</style>