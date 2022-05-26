<template>
<div>
<form @submit.prevent="onSubmit">
  <div>
      <label for="nickname">nickname : </label>
      <input v-model="newProfile.nickname" type="text" id="nickname" />
  </div>
  <div>
    <button>Update</button>
  </div>
</form>

</div>

</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'UserInfoForm',
  props: {
    profile : Object,
  },
  data() {
    return {
      newProfile : {
        nickname : this.profile.nickname
      }
    }
  },
  methods : {
    ...mapActions(['updateUser']),
    onSubmit(){
        const payload = {username : this.profile.username, nickname : this.newProfile.nickname
          }
          this.updateUser(payload)
      }
    },
}
</script>

<style>

</style>