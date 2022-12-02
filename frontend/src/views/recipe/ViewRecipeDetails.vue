<template>
<navbar></navbar>
{{name}}
{{description}}
{{price}}

<img :src="image" alt="zdjecie" class="rounded-circle" style="width:200px;">
<div v-for="product in product_list">
{{product.name}}
</div>
</template>


<script>
import axios from "axios";
import Navbar from "@/components/ui/Navbar.vue";
import FormData from "form-data";

export default {
    components: {
        Navbar,
    },
    data() {
        return {
            name: "",
            price: "",
            description: "",
            token: "",
            image: "",
            recipe: "",
            product_list: [],

        }
    },
    computed: {
        getToken() {
            return this.$store.state.token;
        }
    },
    mounted() {
        const recipe_id = this.$route.params.id;   //? pobranie id przepisu z parametru - URL
        this.getRecipe();
    },
    methods: {
        getRecipe(){
            const recipe_id = this.$route.params.id;   //? pobranie id przepisu z parametru - URL
            let formData = new FormData();
            //formData.append('id', product_id);
            axios
                .get(`/api/v1/recipe/${recipe_id}/`, {
                    headers: {
                        Authorization: `Token ${this.$store.state.user.token}`
                    }
                })
                .then((response) => {
                    this.name = response.data.name;
                    this.description = response.data.description;
                    this.price = response.data.price;
                    this.image = response.data.get_image;
                    this.product_list = response.data.product_list;
                    this.recipe = response.data;
                })
                .catch((error) => {
                    console.log(error);
                })
        },
    }
}
</script>