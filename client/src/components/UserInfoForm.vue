<template>
<div>
<form @submit.prevent="onSubmit">
  <div>
      <!-- <label for="nickname">nickname : </label> -->
      <input class="input-label" v-model="newProfile.nickname" type="text" id="nickname" />
  </div>
  <div>
    <button class="btn-update">Update</button>
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

<style scoped>
.input-label{
  margin-top: 10px;
	width: 330px;
	height: 50px;
	background: transparent;
	border: 2px solid #0b1b38;
	border-radius: 2px;
	color: #0b1b38;
	font-family: 'Exo', sans-serif;
	font-size: 30px;
	font-weight: 400;
	padding: 4px;
}


.btn-update{
	width: 330px;
	height: 50px;
	background: #0b1b38;
	border: 1px solid #0b1b38;
	cursor: pointer;
	border-radius: 2px;
	color: #fff;
	font-family: 'Exo', sans-serif;
	font-size: 25px;
	font-weight: 400;
	padding: 4px;
	margin-top: 10px;
}
</style>