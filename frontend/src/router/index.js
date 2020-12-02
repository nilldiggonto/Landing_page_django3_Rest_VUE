import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Question from "../views/Question.vue"
import QuestionEditor from "../views/QuestionEditor.vue"
import AnswerEditor from "../views/AnswerEditor.vue"

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path:'/question/:slug',
    name:'Question_d',
    component: Question,
    props: true
  },
  {
    path:'/ask/:slug?',
    name:'Question_Edit',
    component: QuestionEditor,
    props: true
  },
  {
    path:'/answer/:id',
    name:'Answer_Edit',
    component: AnswerEditor,
    props: true
  },









  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
