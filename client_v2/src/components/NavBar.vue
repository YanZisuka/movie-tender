<template>
  <nav class="d-flex justify-content-between sticky-top p-3">
    <router-link :to="{ name: 'index' }" class="navbar-brand mx-5">
      <div :class="isDark ? 'text-fff' : 'text-theme'" class="navbar-logo">
        movietender
      </div>
    </router-link>
    <div class="d-flex align-items-center">
      <router-link
        :to="{ name: 'movies' }"
        :class="isDark ? 'text-fff' : 'text-theme'"
        class="text-decoration-none mx-5"
        v-if="isLoggedIn"
        >OMAKASE</router-link
      >

      <router-link
        :to="{ name: 'reviews' }"
        :class="isDark ? 'text-fff' : 'text-theme'"
        class="text-decoration-none mx-5"
        >COMMUNITY</router-link
      >

      <div v-if="isLoggedIn" class="dropdown mx-5">
        <button
          :class="isDark ? 'text-fff' : 'text-theme'"
          class="btn dropdown-toggle"
          type="button"
          id="dropdownMenuButton"
          data-toggle="dropdown"
          aria-haspopup="true"
          aria-expanded="false"
        >
          <img class="profile-img me-2" :src="profileImg" alt="profile-img" />
        </button>

        <div class="profile dropdown-menu" aria-labelledby="dropdownMenuButton">
          <router-link
            :to="{
              name: 'profile',
              params: { username: currentUser.username },
            }"
            class="text-decoration-none"
            role="button"
          >
            <p class="text-fff text-center m-0">Profile</p>
          </router-link>
          <hr class="text-white m-1" />
          <router-link
            :to="{ name: 'logout', params: { username: currentUser.username } }"
            class="text-decoration-none"
            role="button"
          >
            <p class="text-fff text-center m-0">Logout</p>
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
        >
          <i class="fa-solid fa-xmark"></i>
        </button>
        <login-modal
          v-if="!isSignUp"
          @signup-emit="isSignUp = true"
        ></login-modal>
        <signup-modal v-else @login-emit="isSignUp = false"></signup-modal>
      </div>
    </modal-detail>
  </nav>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

import ModalDetail from "@/components/ModalDetail.vue";
import LoginModal from "@/components/LoginModal.vue";
import SignupModal from "@/components/SignupModal.vue";

import profileImg from "@/assets/default-profile.png";

export default {
  name: "NavBar",

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
      profileImg: profileImg,
      isSignUp: false,
    };
  },

  computed: {
    ...mapGetters([
      "isLoggedIn",
      "currentUser",
      "authError",
      "showAccountModal",
    ]),
  },

  methods: {
    ...mapActions(["switchShowAccountModal"]),
  },
};
</script>

<style scoped>
nav {
  padding: 2rem;
}
nav a {
  font-weight: 700;
  color: var(--black);
}
nav a.router-link-exact-active {
  color: var(--mainBgColor);
}
.navbar-logo {
  font-family: "Lobster", cursive;
  font-size: 2rem;
}
.navbar-btn {
  background-color: var(--mainBgColor);
  width: 5rem;
  height: 28px;
  border-radius: 16px;
  border: 0;
  color: var(--white);
}
.profile {
  background-color: rgba(0, 0, 0, 0.5);
  border: 0;
  margin: 0 75px 0 0;
}
.profile-img {
  width: 2rem;
}
.text-fff {
  color: var(--white);
}
.text-theme {
  color: var(--black);
}
.modal-body {
  display: inline-block;
  background: var(--white);
  /* border: 2px solid var(--black); */
  filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
  border-radius: 16px;
}
</style>
