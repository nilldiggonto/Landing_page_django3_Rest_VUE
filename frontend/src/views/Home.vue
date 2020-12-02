<template>
  <div class="home">
    <div class="container">
      <!-- <img alt="Vue logo" src="../assets/logo.png" /> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App" /> -->

    <div class="card mt-2 mb-2 border-primary" v-for="question in questions" :key="question.pk">
    
      <div class="card-body">
        <blockquote class="blockquote text-center">
        <!-- <p class="mb-0">{{question.content}}</p> -->
        <router-link style="text-decoration:none;font-size:30px;" class="mb-0" :to="{name:'Question_d',params:{slug: question.slug}}"> 
          {{question.content}}
        </router-link>
        
        <footer class="blockquote-footer">@{{question.author}} |
           <strong>
             <span class="text-info">Answer: {{question.answer_count}}</span>
           </strong>
           </footer>
         
      </blockquote>
      </div>
    </div>
    <p v-show="loadingQuestions">Loading............</p>
    <button v-show="next" @click="getQuestion" class="btn btn-primary btn-block">Load More</button>


    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";


//API Servie
import {apiService} from '../common/api.service'

export default {
  name: "Home",
  data(){
    return {
      questions: [],
      next: null,
      loadingQuestions:false
    }
  },
  methods:{
    getQuestion(){
      let endpoint = `/api/q/questions/`;
      if (this.next){
        endpoint = this.next;
      }
      this.loadingQuestions = true
      apiService(endpoint).then(data=>{
        this.questions.push(...data.results);
        this.loadingQuestions= false;
        if (data.next){
          this.next = data.next;
        }
        else{
          this.next = null;
        }
      })
    }
  },
  created(){
    this.getQuestion()
    console.log(this.questions)
    document.title = 'Ask Anything'
  }

};
</script>
