<template>
  <div>
    <account-error-list v-if="authError"></account-error-list>
    <div class="header">
      <div>movie<span>tender</span></div>
    </div>
    <div class="login">
      <form @submit.prevent="login(credentials)">
        <div>
          <input class="input-label first-input" v-model="credentials.username" type="text" id="username" placeholder=" Username" required />
        </div>
        <div>
          <input class="input-label" v-model="credentials.password" type="password" id="password" placeholder=" Password" required />
        </div>
        <div>
          <button class="btn-login">Login</button>
        </div>
      </form>
      <router-link :to="{ name: 'signup'}">
        <p>회원가입 하러가기</p>
      </router-link>
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
  name : 'LoginView',
  data() {
    return {
      credentials : {
        username : '',
        password : ''
      }
    }
  },
  computed : {
    ...mapGetters(['authError'])
  },
  methods : {
    ...mapActions(['login'])
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

.login{
	position: absolute;
  top: calc(50% + 160px);
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

.btn-login{
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

p {
  color : #0b1b38;
  margin-top: 3px;
  float: right;
}
</style>