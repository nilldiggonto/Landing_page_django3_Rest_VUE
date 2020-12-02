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
      </div>
    </div>


    </div>
</template>

<script>
import {apiService} from '../common/api.service'
export default {
    name: 'Question',
    props:{
        slug:{
            type:String,
            required: true,
        }
    },
    data(){
        return{
            question:{}
        }
    },
    methods:{
        setPageTitle(title){
            document.title = title;
        },
        getQuestionData(){
            let endpoint = `/api/q/questions/${this.slug}/`;
            apiService(endpoint).then(data=>{
                this.question = data;
                this.setPageTitle(data.content)
            })
        }
    },
    created(){
        this.getQuestionData()
        console.log(this.question)
    }
}
</script>

<style >

</style>