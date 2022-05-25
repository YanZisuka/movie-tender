<template>
  <div>
    <movie-keyword-survey></movie-keyword-survey>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import MovieKeywordSurvey from '@/components/MovieKeywordSurvey.vue'

export default {
  components: {
    MovieKeywordSurvey,
  },

  name: 'MovieSurveyView',

  data() {
    return {}
  },

  computed: {
    ...mapGetters(['profile'])
  },

  methods: {},

  created() {},
}
</script>

<style>

</style>