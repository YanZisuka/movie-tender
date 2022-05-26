<template>
  <div>
    <h1>Edit Profile</h1>
  <user-info-form :profile="profile"> </user-info-form>
  </div>
</template>

<script>
import UserInfoForm from '@/components/UserInfoForm.vue'
import { mapGetters, mapActions } from 'vuex'

export default {
  name : 'ProfileEditView',
  components : { UserInfoForm },
  data(){
      return {
          username : this.$router.params.username
      }
  },
  computed : {
    ...mapGetters(['profile', 'currentUser']),
  },
  methods: {
    ...mapActions(['fetchProfile'])
  },
  created() {
    this.fetchProfile(this.username)
  },
}
</script>

<style>

</style>