<template>
  <nav class="d-flex justify-content-between sticky-top p-3">
    <router-link :to="{ name: 'index' }" class="navbar-brand mx-5">
      <div :class="isDark ? 'text-white' : 'text-theme'" class="navbar-logo">movietender</div>
    </router-link>
    <div class="d-flex align-items-center">

      <router-link
        :to="{ name: 'movies' }"
        :class="isDark ? 'text-white' : 'text-theme'"
        class="text-decoration-none mx-5"
        >OMAKASE</router-link>

      <router-link
        :to="{ name: 'reviews' }"
        :class="isDark ? 'text-white' : 'text-theme'"
        class="text-decoration-none mx-5"
        >COMMUNITY</router-link>

      <div v-if="isCurrentUser" class="dropdown mx-5">
        <button
          :class="isDark ? 'text-white' : 'text-theme'"
          class="btn dropdown-toggle"
          type="button"
          id="dropdownMenuButton"
          data-toggle="dropdown"
          aria-haspopup="true"
          aria-expanded="false">
          <img class="profile-img me-2" :src="profileImg" alt="profile-img">
        </button>

        <div class="profile dropdown-menu me-5" aria-labelledby="dropdownMenuButton">
            <router-link
              :to="{ name: 'profile', params: { username: currentUser.username } }"
              class="text-decoration-none"
              role="button">
              <p class="text-center m-0">
              Profile
              </p>
            </router-link>
            <hr class="m-1">
            <router-link
              :to="{ name: 'logout', params: { username: currentUser.username } }"
              class="text-decoration-none"
              role="button">
              <p class="text-center m-0">
              Logout
              </p>
            </router-link> 
        </div>
      </div>

      <button v-else @click="switchShowAccountModal()" class="navbar-btn mx-5">
        Login
      </button>
    </div>

    <modal-detail
      :show="showAccountModal"
      @close="switchShowAccountModal()"
      >
      <div slot="body">
        <account-error-list v-if="authError"></account-error-list>

        <div class="login-body d-flex flex-column text-start p-5">

          <h1>LOGIN</h1>

          <form @submit.prevent="login(credentials); switchShowAccountModal();">
            <div class="my-4">
              <div>
                <label for="username">아이디</label>
              </div>
              <input v-model="credentials.username" type="text" id="username" placeholder="ID" required>
            </div>

            <div class="my-4">
              <div>
                <label for="password">비밀번호</label>
              </div>
              <input v-model="credentials.password" type="password" id="password" placeholder="Password" required>
            </div>

            <p>아직 회원이 아니신가요? 회원가입</p>

            <button class="btn-theme mt-3">로그인</button>
          </form>

        </div>

      </div>
    </modal-detail>

  </nav>
</template>

<script>
import _ from 'lodash'
import { mapGetters, mapActions } from 'vuex'

import ModalDetail from '@/components/ModalDetail.vue'
import AccountErrorList from '@/components/AccountErrorList.vue'

export default {
  name: 'NavBar',

  components: {
    ModalDetail,
    AccountErrorList,
  },

  props: {
    isDark: Boolean,
  },

  data() {
    return {
      profileImg: require('@/assets/default-profile.png'),
      credentials: {
        username: '',
        password: '',
      },
    }
  },

  computed: {
    ...mapGetters(['currentUser', 'authError', 'showAccountModal',]),
    isCurrentUser() {
      return !_.isEmpty(this.currentUser)
    },
  },

  methods: {
    ...mapActions(['login', 'switchShowAccountModal',]),
  },

  created() {}

}
</script>

<style scoped>
nav {
  padding: 2rem;
}

nav a {
  font-weight: bold;
  color: #0b1b38;
}

nav a.router-link-exact-active {
  color: #cf1224;
}

.navbar-logo {
  font-family: 'Lobster', cursive;
  font-size: 2rem;
}

.navbar-btn {
  background-color: #0b1b38;
  width: 5rem;
  height: 28px;
  border-radius: 16px;
  border: 0;
  color: white;
}

.profile {
  background-color: rgba(255, 255, 255, 0.3);
  border: 0;
}

.profile-img {
  width: 2rem;
}

.text-theme {
  color: #0b1b38;
}

.login-body h1 {
  font-weight: 700;
}

.login-body label {
  font-weight: 700;
  margin: 0 0 3px 0;
}

.login-body input {
  width: 20rem;
  height: 2.5rem;
  border: 2px solid #ddd;
  border-radius: 8px;
  padding: 1rem;
}
</style>