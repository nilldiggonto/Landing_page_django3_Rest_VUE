<template>
        <div class="container">
      <!-- <img alt="Vue logo" src="../assets/logo.png" /> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App" /> -->

    <div class="card mt-2" >
    
      <div class="card-body">
        <blockquote class="blockquote text-left">
        <h1 class="mb-0">{{question.content}}</h1>
       
      
        <footer class="blockquote-footer">@{{question.author}} |
           <strong>
             <span class="text-info">Created at: {{question.created_at}}</span>
           </strong>
           </footer>
         
      </blockquote>

      <QuestionAction v-if="isQuestionAuthor" :slug="question.slug"/>
      </div>
      <div class="card-footer">
           <div v-if="userHasAnswered">
               <p>You have written an answer!</p>
           </div>
           <div v-else-if="showForm">
               <form action="" class="card" @submit.prevent="onSubmit">
                   <div class="card-header">
                       <h4>Answer the question</h4>
                   </div>
                   <div class="card-body">
                       <textarea class="form-control" v-model="newAnswerBody" 
                       name="" id="" cols="30" rows="5" placeholder="type the answer here">
                       </textarea>
                   </div>
                   <div class="card-footer">
                       <button type="submit" class="btn btn-sm btn-block btn-success">Answer</button>
                   </div>
                   <p class="text-danger" v-if="error">{{error}}</p>
               </form>
           </div>
           <div v-else>
               <button class="btn btn-sm btn-primary" @click="showForm=true">I got the answer!</button>
           </div>
      </div>
      <div class="card-footer" >
          <AnswerComponent @delete-answer="deleteAnswer" :requestUser="requestUser" v-for="answer in answers" :key="answer.id" :answer="answer"/>

          
      </div>
      
    </div>
  <p v-show="loadingAnswers">Loading............</p>
         <button v-show="next" @click="getQuestionAnswers" class="btn btn-primary btn-block">Load More</button>

    </div>
</template>

<script>
import {apiService} from '../common/api.service'
import AnswerComponent from '@/components/Answer.vue'
import QuestionAction from "@/components/QuestionAction"
export default {
    name: 'Question',
    props:{
        slug:{
            type:String,
            required: true,
        }
    },
    components:{
        AnswerComponent,
        QuestionAction
    },
    data(){
        return{
            question:{},
            answers : [],
            newAnswerBody: null,
            error:null,
            userHasAnswered:false,
            showForm:false,
            next:null,
            loadingAnswers:false,
            requestUser:null,
            
        }
    },
    computed:{
        isQuestionAuthor(){
            return this.question.author == this.requestUser;
        }
    },
    methods:{
        setPageTitle(title){
            document.title = title;
        },
        setRequestUser(){
            this.requestUser = window.localStorage.getItem('username')
        },
        getQuestionData(){
            let endpoint = `/api/q/questions/${this.slug}/`;
            apiService(endpoint).then(data=>{
                this.question = data;
                this.userHasAnswered = data.user_has_answered
                this.setPageTitle(data.content)
            })
        },
        getQuestionAnswers(){
            let endpoint = `/api/q/questions/${this.slug}/answer/list/`;
            if (this.next) {
                endpoint =this.next;
            }
            this.loadingAnswers= true;
            apiService(endpoint).then(data=>{
                this.answers.push(...data.results);
                this.loadingAnswers = false;
                if(data.next){
                    this.next = data.next
                }
                else{
                    this.next = null
                }
            })
        },
        onSubmit(){
            if (this.newAnswerBody){
                let endpoint = `/api/q/questions/${this.slug}/answer/`;
                apiService(endpoint,'POST',{body:this.newAnswerBody}).then(data=>{
                    this.answers.unshift(data)
                })
                this.newAnswerBody = null
                this.showForm = false
                this.userHasAnswered = true
                if (this.error){
                    this.error = null;
                }
            }
            else{
                this.error = "First write something!!"
            }
        },
        async deleteAnswer(answer){
            let endpoint = `/api/q/answer/${answer.id}/`;
            try{
                await apiService(endpoint,'DELETE')
                this.$delete(this.answers,this.answers.indexOf(answer))
                this.userHasAnswered = false;
            }
            catch(err){
                console.log(err)
            }
        }
    },
    created(){
        this.getQuestionData()
        console.log(this.question)
        this.getQuestionAnswers()
        this.setRequestUser()
    }
}
</script>

<style >

</style>