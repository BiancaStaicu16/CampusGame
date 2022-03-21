import ChangePassword from "@/views/ChangePassword";
import Community from "../views/Community.vue";
import EnterNewPassword from "../views/EnterNewPassword";
import Feed from "../views/Feed.vue";
import ForgotPassword from "@/views/ForgotPassword";
import Profile from "../views/Profile.vue"
import Leaderboard from "../views/Leaderboard.vue";
import LoginPage from "../views/LoginPage.vue";
import NotFound from "@/views/NotFound";
import RegisterPage from "../views/RegisterPage.vue";
import Settings from "@/views/Settings";
import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Feed",
    component: Feed,
  },
  {
    path: "/login",
    name: "LoginPage",
    component: LoginPage,
  },
  {
    path: "/login/forgot",
    name: "ForgotPassword",
    component: ForgotPassword,
  },
  {
    path: "/login/passwordreset",
    name: "EnterNewPassword",
    component: EnterNewPassword,
  },
  {
    path: "/register",
    name: "RegisterPage",
    component: RegisterPage,
  },

  {
    path: "/leaderboard",
    name: "Leaderboard",
    component: Leaderboard,
  },
  {
    path: "/communities",
    name: "Community",
    component: Community,
  },
  {
    path: "/profile",
    name: "Profile",
    component: Profile,
  },
  {
    path: "/settings",
    name: "Settings",
    component: Settings,
  },

  {
    path: "*",
    name: "NotFound",
    component: NotFound,
  },
  {
    path: "/changePassword",
    name: "ChangePassword",
    component: ChangePassword,
  },
];

const router = new VueRouter({
  mode: "history",
  routes,
});


export default router;