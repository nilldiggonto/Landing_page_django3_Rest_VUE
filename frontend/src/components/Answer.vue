<template>
  <div class="container">
    <blockquote class="blockquote text-left">
      <footer class="blockquote-footer">
        {{ answer.author }}
        <cite title="Source Title">{{ answer.created_at }}</cite>
      </footer>
      <p class="mb-0 text-dark">{{ answer.body }}</p>
    </blockquote>

    <div v-if="isAnswerAuthor">
        <!-- <button class="btn btn-sm btn-warning" type="submit">Edit</button> -->
        <router-link  class="btn btn-sm btn-warning" :to="{name:'Answer_Edit', params:{id:answer.id}}"
        >Edit
         </router-link>
        <button @click="triggerDeleteAnswer" class="btn btn-sm btn-primary ml-2" type="submit">Delete</button>
    </div>


      <div v-else >
      <button @click="toggleLike" :class="{'btn-danger':userLikedAnswer,
              'btn-outline-danger': !userLikedAnswer}" class="btn btn-sm">Liked {{likeCounter}}</button>
    </div>
    <hr />
  

    <!-- <p class="text-muted">
            <strong>{{answer.author}}</strong> &#8901; {{answer.created_at}}
        </p>
        <p>
            {{answer.body}}
        </p> -->
  </div>
</template>

<script>
import {apiService} from '../common/api.service'
export default {
  name: "AnswerComponent",
  props: {
    answer: {
      type: Object,
      required: true,
    },
    requestUser: {
      type: String,
      required: true,
    },
  },
  data(){
    return{
      userLikedAnswer: this.answer.user_has_voted,
      likeCounter: this.answer.likes_count
    }
  },
  computed: {
    isAnswerAuthor() {
      return this.answer.author == this.requestUser;
    },
  },
  methods:{

      toggleLike(){
        this.userLikedAnswer === false ? this.likedAnswer(): this.unLikedAnswer()
      },
      likedAnswer(){
        this.userLikedAnswer = true
        this.likeCounter += 1
        let endpoint = `/api/q/answer/${this.answer.id}/like/`;
        apiService(endpoint,'POST')
      },
      unLikedAnswer(){
        this.userLikedAnswer = false
        this.likeCounter -= 1
        let endpoint = `/api/q/answer/${this.answer.id}/like/`;
        apiService(endpoint,'DELETE')
      },
      triggerDeleteAnswer(){
          this.$emit('delete-answer',this.answer)
      }
  }
};
</script>