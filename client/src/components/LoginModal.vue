<template>
  <div>
    <div class="login-body d-flex flex-column text-start pt-3 pb-5 px-5">
      <h1 class="">로그인</h1>

      <form @submit.prevent="login(credentials)" class="d-flex flex-column">
        <div class="mt-4 mb-3">
          <div>
            <label for="username" class="">아이디</label>
          </div>
          <input
            v-model="credentials.username"
            type="text"
            id="username"
            placeholder="ID"
            required
          />
        </div>

        <div class="mt-3">
          <div>
            <label for="password" class="">비밀번호</label>
          </div>
          <input
            v-model="credentials.password"
            type="password"
            id="password"
            placeholder="Password"
            required
          />
        </div>

        <div class="mt-1 mb-2">
          <span @click="$emit('signup-emit')" class=""
            >아직 회원이 아니신가요? 회원가입</span
          >
        </div>

        <button class="button align-self-center mt-5">로그인</button>
      </form>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "LoginModal",

  data() {
    return {
      credentials: {
        username: "",
        password: "",
      },
    };
  },

  computed: {
    ...mapGetters(["authError"]),
  },

  methods: {
    ...mapActions(["login", "switchShowAccountModal"]),
  },
};
</script>

<style scoped lang="scss">
.login-body {
  h1 {
    font-weight: bold;
    font-size: 2rem;
  }
  label {
    font-weight: normal;
    margin: 0 0 3px 0;
  }
  input {
    height: 2.5rem;
    padding: 0 1rem;
  }
  span {
    &:hover {
      cursor: pointer;
      text-decoration-line: underline;
    }
  }
}
</style>
