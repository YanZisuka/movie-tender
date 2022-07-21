<template>
  <div>

    <div class="login-body d-flex flex-column text-start pt-3 pb-5 px-5">
    <account-error-list v-if="authError"></account-error-list>

      <h1 class="">로그인</h1>

      <form @submit.prevent="login(credentials); switchShowAccountModal();" class="d-flex flex-column">
        <div class="my-4">
          <div>
            <label for="username" class="">아이디</label>
          </div>
          <input v-model="credentials.username" type="text" id="username" placeholder="ID" required>
        </div>

        <div class="mt-4">
          <div>
            <label for="password" class="">비밀번호</label>
          </div>
          <input v-model="credentials.password" type="password" id="password" placeholder="Password" required>
        </div>

        <div class="mt-1 mb-2">
          <span @click="$emit('signup-emit')" class="">아직 회원이 아니신가요? 회원가입</span>
        </div>

        <button class="btn-theme align-self-center mt-5">로그인</button>
      </form>

    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

import AccountErrorList from '@/components/AccountErrorList.vue'

export default {
  name: 'LoginModal',

  components: {
    AccountErrorList,
  },

  data() {
    return {
      credentials: {
        username: '',
        password: '',
      },
    }
  },

  computed: {
    ...mapGetters(['authError']),
  },

  methods: {
    ...mapActions(['login', 'switchShowAccountModal',])
  },

}
</script>

<style scoped>
.login-body h1 {
  font-weight: 700;
}

.login-body label {
  font-weight: 700;
  margin: 0 0 3px 0;
}

.login-body input {
  width: 100%;
  height: 2.5rem;
  border: 2px solid var(--gray);
  border-radius: 8px;
  padding: 0 1rem;
}

.login-body span:hover {
  cursor: pointer;
  text-decoration-line: underline;
}
</style>