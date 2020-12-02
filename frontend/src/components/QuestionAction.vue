<template>
        
        <div>
            <!-- <button class="btn btn-sm btn-warning" type="submit">Edit</button> -->
        <router-link  class="btn btn-sm btn-warning" :to="{name:'Question_Edit', params:{slug:slug}}"
        >Edit
         </router-link>
        <button @click="deleteQuestion" class="btn btn-sm btn-primary ml-2" type="submit">
            Delete
        </button>
        </div>
   
</template>

<script>
import {apiService} from '../common/api.service'
export default {
    name: 'QuestionAction',
    props:{
        slug:{
            type:String,
            required:true,
        }
    },
    methods:{
        async deleteQuestion(){
            let endpoint = `/api/q/questions/${this.slug}/`;
            try{
                await apiService(endpoint,'DELETE');
                this.$router.push('/')
            }
            catch(err){
                console.log(err)
            }
        }

    }
}
</script>