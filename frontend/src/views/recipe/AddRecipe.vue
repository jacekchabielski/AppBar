<template>
    <navbar></navbar>
    dodawanie przepisu
    
</template>

<script>
import axios from "axios";
import Navbar from "@/components/ui/Navbar.vue";
import { ref } from "vue";

export default{
    components: {
        Navbar,
    }
}
</script>