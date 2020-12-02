<template>
    <div class="container">

        <blockquote class="blockquote text-left">
  
  <footer class="blockquote-footer">{{answer.author}} <cite title="Source Title">{{answer.created_at}}</cite></footer>
  <p class="mb-0 text-dark">{{answer.body}}</p>
</blockquote>
<hr>


        <!-- <p class="text-muted">
            <strong>{{answer.author}}</strong> &#8901; {{answer.created_at}}
        </p>
        <p>
            {{answer.body}}
        </p> -->
    </div>
</template>

<script>
export default {
    name : 'AnswerComponent',
    props:{
        answer:{
            type:Object,
            required: true,
        }
    }
}
</script>