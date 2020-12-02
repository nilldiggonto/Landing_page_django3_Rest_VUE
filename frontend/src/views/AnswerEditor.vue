<template>
    <div class="container mt-4">
        <div class="card">
            <div class="card-header">
                <h2>Want to change answer?</h2>
            </div>
            <div class="card-body">
                <form action="" class="form" @submit.prevent="onSubmit">
                    <textarea placeholder="Answer anything!!"
                     name="" id="" cols="30" rows="3" class="form-control" v-model="answerBody">

                    </textarea>

                    <button type="submit" class="btn btn-primary btn-block mt-1">Answer</button>
                    <p class=" text-danger" v-if="error">{{error}}</p>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
//API Servie
import {apiService} from '../common/api.service'

export default {
    name:'AnswerEditor',
    props:{
        id:{
            type:Number,
            required: true
        },
        questionSlug:{
            type:String,
            required:true
        },
        previousAnswer:{
            type:String,
            required:true
        },
    
    },
    data(){
        return{
            answerBody: this.previousAnswer,
            error:null,
        }
    },
    methods:{
        onSubmit(){
            if (this.answerBody){
                let endpoint = `/api/q/answer/${this.id}/`
                apiService(endpoint,'PUT',{body: this.answerBody}).then( ()=>{
                    this.$router.push({
                        name:'Question_d',
                        params: {slug:this.questionSlug}
                    })
                })
            }
            else{
                this.error = 'To submit write something'
            }
        }
    },
    async beforeRouteEnter(to,from,next){
        let endpoint = `/api/q/answer/${to.params.id}/`;
        let data = await apiService(endpoint,'GET')
        to.params.previousAnswer = data.body;
        to.params.questionSlug = data.question_slug
        return next()
    }

}
</script>