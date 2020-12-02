<template>
    <div class="container mt-4">
        <div class="card">
            <div class="card-header">
                <h2>What do you want to ask?</h2>
            </div>
            <div class="card-body">
                <form action="" class="form" @submit.prevent="onSubmit">
                    <textarea placeholder="Ask anything!!"
                     name="" id="" cols="30" rows="3" class="form-control" v-model="question_body">

                    </textarea>

                    <button type="submit" class="btn btn-primary btn-block mt-1">Ask</button>
                    <p class=" text-danger" v-if="error">{{error}}</p>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import {apiService} from '../common/api.service'
export default {
    name: 'QuestionEditor',
    data(){
        return {
            question_body: null,
            error:null,
        }
    },
    methods:{
        onSubmit(){
            if (!this.question_body){
                this.error = "You have to ask something!!"
            }
            else if (this.question_body.length >200){
                this.error = "We can't add more than 200 Characters"
            }
            else{
                let endpoint = "/api/q/questions/"
                let method =  "POST"
                apiService(endpoint,method,{content:this.question_body}).then(question_data=>{
                    this.$router.push(
                        {name:'Question_d',
                        params: {slug:question_data.slug}}
                    )
                })
            }
        }
    },
    created(){
        document.title = 'Editor'
    }
}
</script>