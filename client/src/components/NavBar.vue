<template>
  <nav class="row d-flex sticky-top">
    <auth-error v-if="authError"></auth-error>

    <div class="d-flex col-6">
      <router-link :to="{ name: 'index' }" class="navbar-brand">
        <h1 :class="isDark ? 'text-fff' : 'text-theme'" class="navbar-logo">
          movietender
        </h1>
      </router-link>
      <router-link
        :to="{ name: 'movies' }"
        :class="isDark ? 'text-fff' : 'text-theme'"
        class="text-decoration-none pt-2 ms-5"
        v-if="isLoggedIn"
        >영화추천
      </router-link>
    </div>
    <div class="d-flex justify-content-end align-items-center col-6">
      <!-- <router-link
        :to="{ name: 'reviews' }"
        :class="isDark ? 'text-fff' : 'text-theme'"
        class="text-decoration-none"
        >COMMUNITY</router-link
      > -->

      <div
        v-if="isLoggedIn"
        class="profile"
        @mouseenter="setIsDisplayProfileMenu(true)"
        @click="setIsDisplayProfileMenu(true)"
        @mouseleave="setIsDisplayProfileMenu(false)"
      >
        <img class="profile-img me-3" :src="profileImg" alt="profile-img" />
        <i class="fa-solid fa-chevron-down"></i>

        <div v-if="isDisplayProfileMenu" class="menu">
          <div class="d-flex w-100">
            <img :src="profileImg" alt="" />
            <div class="d-flex flex-column justify-content-center ms-2">
              <h1>{{ profile.nickname }}</h1>
              <h2>{{ profile.username }}</h2>
            </div>
          </div>
          <hr />
          <router-link
            :to="{ name: 'logout', params: { username: currentUser.username } }"
            class="text-decoration-none"
          >
            <button>로그아웃</button>
          </router-link>
        </div>
      </div>

      <!-- <router-link
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
      </div> -->

      <button v-else @click="switchShowAccountModal()" class="navbar-btn">
        로그인/회원가입
      </button>
    </div>

    <!-- modal component -->
    <modal-detail :show="showAccountModal">
      <div slot="body" class="modal-body d-flex flex-column">
        <button
          class="align-self-end mt-2 me-2"
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

import AuthError from "@/components/AuthError.vue";
import ModalDetail from "@/components/ModalDetail.vue";
import LoginModal from "@/components/LoginModal.vue";
import SignupModal from "@/components/SignupModal.vue";

export default {
  name: "NavBar",

  components: {
    AuthError,
    ModalDetail,
    LoginModal,
    SignupModal,
  },

  props: {
    isDark: Boolean,
  },

  data() {
    return {
      profileImg: require("@/assets/default-profile.png"),
      isSignUp: false,
      isDisplayProfileMenu: false,
    };
  },

  computed: {
    ...mapGetters([
      "isLoggedIn",
      "currentUser",
      "profile",
      "authError",
      "showAccountModal",
    ]),
  },

  methods: {
    ...mapActions([
      "fetchCurrentUser",
      "fetchProfile",
      "switchShowAccountModal",
    ]),
    setIsDisplayProfileMenu(payload) {
      this.isDisplayProfileMenu = payload;
    },
  },

  async created() {
    await this.fetchCurrentUser();
    this.fetchProfile(this.currentUser);
  },
};
</script>

<style scoped lang="scss">
nav {
  height: 85px;
  padding: 0 2rem;

  @include lg {
    padding: 0 5rem;
  }

  a {
    font-weight: bold;
    color: $blackColor;
    display: flex;
    align-items: center;
    font-size: 0.9rem;
  }

  a.router-link-exact-active {
    color: $mainBadgeColor;
  }
}
.navbar-logo {
  font-family: "Lobster", cursive;
  font-size: 2rem;
}
.navbar-btn {
  background-color: transparent;
  height: 2rem;
  border-radius: 16px;
  border: 0;
  font-weight: bold;
  color: $whiteColor;

  &:hover {
    color: $adaptiveGrey200;
  }
}
.profile {
  margin-left: 5rem;
  color: $adaptiveGrey100;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;

  &:hover {
    cursor: pointer;

    i {
      transform: rotate(180deg);
      transition: transform 0.15s ease;
    }
  }
}
.profile-img {
  width: 2rem;
  border-radius: 4px;
}
.text-theme {
  color: $blackColor;
}
.modal-body {
  display: inline-block;
  background: $whiteColor;
  /* border: 2px solid var(--black); */
  filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
  border-radius: 16px;

  button {
    background-color: transparent;
    border: 0;
    color: $adaptiveGrey800;

    &:hover {
      color: $adaptiveGrey500;
    }
  }
}
.menu {
  width: 10rem;
  background-color: $offwhiteColor;
  position: absolute;
  top: 33px;
  right: 0;
  border-radius: 4px;
  color: $blackColor;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 0.3rem 0.1rem;
  filter: drop-shadow(0 0 1rem $blackColor);
  overflow: hidden;
  text-overflow: ellipsis;
  padding: 1rem 0.5rem 0.5rem 0.5rem;

  img {
    width: 2.5rem;
    border-radius: 4px;
  }
  h1 {
    font-size: 1.2rem;
    font-weight: bold;
  }
  hr {
    width: 100%;
    margin: 0.5rem;
  }
  button {
    border: 0;
    background-color: transparent;
  }
}
</style>
