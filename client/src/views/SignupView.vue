<template>
  <div class="grad">
    <div class="header">
    <div>movie<span>tender</span></div>
    </div>
    <br>
    <account-error-list v-if="authError"> </account-error-list>
    <div class="signup">
      <form @submit.prevent="signup(credentials)">
        <div>
          <input class="input-label first-input" v-model="credentials.username" type="text" id="username" placeholder=" Username" required/>
        </div>
        <div>
          <input class="input-label" v-model="credentials.nickname" type="text" id="nickname" placeholder=" Nickname" required/>
        </div>
        <div>
          <input class="input-label" v-model="credentials.password1" type="password" id="password1" placeholder=" Password" required />
        </div>
        <div>
          <input class="input-label" v-model="credentials.password2" type="password" id="password2" placeholder=" Password Confirmation" required />
        </div>
        <div>
          <button class="btn-singup">Singup</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import AccountErrorList from '@/components/AccountErrorList.vue'

export default {
  components : {
    AccountErrorList
    },
  name : 'SignupView',
  data() {
    return {
      credentials : {
        username : '',
        password1 : '',
        password2 : '',
        nickname : '',
      }
    }
  },
  computed : {
    ...mapGetters(['authError'])
  },
  methods : {
    ...mapActions(['signup'])
  },
}
</script>

<style scoped>

.header{
	position: absolute;
	top: calc(50% + 200px);
	left: calc(50% - 400px);
}

.header div{
	float: left;
	color: #0b1b38;
  font-family: 'Lobster', cursive;
	font-size: 70px;
	font-weight: 200;
}

.header div span{
	color: #0b1b38 !important;
}

.signup{
	position: absolute;
	top: calc(50% + 120px);
	left: calc(50% - 5px);
	height: 150px;
	width: 350px;
	padding: 10px;
}

.input-label{
  margin-top: 10px;
	width: 330px;
	height: 50px;
	background: transparent;
	border: 2px solid #0b1b38;
	border-radius: 2px;
	color: #0b1b38;
	font-family: 'Exo', sans-serif;
	font-size: 20px;
	font-weight: 400;
	padding: 4px;
}

.input-label.first-input{
  margin-top: 0px !important;
}

.btn-singup{
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

.input-label:focus{
	outline: none;
	border: 1px solid #0b1b38;
}

::-webkit-input-placeholder{
  color: #c4c4c4;
  font-family: 'Exo', sans-serif;
}
</style>