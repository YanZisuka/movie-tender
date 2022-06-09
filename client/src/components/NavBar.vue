<template>
  <nav class="d-flex justify-content-between sticky-top p-3">
    <router-link :to="{ name: 'index' }" class="navbar-brand mx-5">
      <div :class="isDark ? 'text-fff' : 'text-theme'" class="navbar-logo">movietender</div>
    </router-link>
    <div class="d-flex align-items-center">

      <router-link
        :to="{ name: 'movies' }"
        :class="isDark ? 'text-fff' : 'text-theme'"
        class="text-decoration-none mx-5"
        >OMAKASE</router-link>

      <router-link
        :to="{ name: 'reviews' }"
        :class="isDark ? 'text-fff' : 'text-theme'"
        class="text-decoration-none mx-5"
        >COMMUNITY</router-link>

      <div v-if="isLoggedIn" class="dropdown mx-5">
        <button
          :class="isDark ? 'text-fff' : 'text-theme'"
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

    <!-- modal component -->
    <modal-detail :show="showAccountModal">
      <div slot="body" class="modal-body d-flex flex-column">
        <button
          class="btn align-self-end mt-2 me-2"
          @click="switchShowAccountModal()"
          ><i class="fa-solid fa-xmark"></i></button>
        <login-modal
          v-if="!isSignUp"
          @signup-emit="isSignUp = true"
          ></login-modal>
        <signup-modal
          v-else
          @login-emit="isSignUp = false"
          ></signup-modal>
      </div>
    </modal-detail>

  </nav>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

import ModalDetail from '@/components/ModalDetail.vue'
import LoginModal from '@/components/LoginModal.vue'
import SignupModal from '@/components/SignupModal.vue'

export default {
  name: 'NavBar',

  components: {
    ModalDetail,
    LoginModal,
    SignupModal,
  },

  props: {
    isDark: Boolean,
  },

  data() {
    return {
      profileImg: require('@/assets/default-profile.png'),
      isSignUp: false,
    }
  },

  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser', 'authError', 'showAccountModal',]),
  },

  methods: {
    ...mapActions(['switchShowAccountModal',]),
  },

  created() {}

}
</script>

<style scoped>
nav {
  padding: 2rem;
}

nav a {
  font-weight: 700;
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
  color: #fff;
}

.profile {
  background-color: rgba(255, 255, 255, 0.3);
  border: 0;
}

.profile-img {
  width: 2rem;
}

.text-fff {
  color: #fff;
}

.text-theme {
  color: #0b1b38;
}

.modal-body {
  display: inline-block;
  background-color: #fbfbfb;
  border-radius: 16px;
}

</style>