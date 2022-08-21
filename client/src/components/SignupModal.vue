<template>
  <div>
    <account-error-list v-if="authError"></account-error-list>

    <div class="signup-body d-flex flex-column text-start pt-3 pb-5 px-5">
      
      <h1 class="">회원가입</h1>

      <form @submit.prevent="signup(credentials); switchShowAccountModal();" class="d-flex flex-column">
        <div class="mt-4 mb-3">
          <div>
            <label for="username" class="">아이디</label>
          </div>
          <input v-model="credentials.username" type="text" id="username" placeholder="ID" required>
        </div>

        <div class="my-3">
          <div>
            <label for="nickname" class="">별명</label>
          </div>
          <input v-model="credentials.nickname" type="text" id="nickname" placeholder="Nickname" required>
        </div>

        <div class="my-3">
          <div>
            <label for="password1" class="">비밀번호</label>
          </div>
          <input v-model="credentials.password1" type="password" id="password1" placeholder="Password" required>
        </div>

        <div class="mt-3">
          <div>
            <label for="password2" class="">비밀번호 확인</label>
          </div>
          <input v-model="credentials.password2" type="password" id="password2" placeholder="Confirm Password" required>
        </div>

        <div class="mt-1 mb-2">
          <span @click="$emit('login-emit')" class="">로그인으로 돌아가기</span>
        </div>

        <button class="btn-theme align-self-center mt-5">회원가입</button>
      </form>

    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

import AccountErrorList from '@/components/AccountErrorList.vue'

export default {
  name: 'SignupModal',

  components: {
    AccountErrorList,
  },

  data() {
    return {
      credentials: {
        username: '',
        password1: '',
        password2: '',
        nickname: '',
      },
    }
  },

    computed: {
    ...mapGetters(['authError']),
  },

  methods: {
    ...mapActions(['signup', 'switchShowAccountModal'])
  },

}
</script>

<style scoped>
.signup-body h1 {
  font-weight: 700;
}

.signup-body label {
  font-weight: 700;
  margin: 0 0 3px 0;
}

.signup-body input {
  width: 20rem;
  height: 2.5rem;
  border: 2px solid var(--border);
  border-radius: 8px;
  padding: 0 1rem;
}

.signup-body span:hover {
  cursor: pointer;
  text-decoration-line: underline;
}
</style>