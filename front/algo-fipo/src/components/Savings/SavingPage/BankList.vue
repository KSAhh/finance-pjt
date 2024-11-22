<template>
    <div class="grid grid-cols-4 gap-4 p-4">
      <div v-for="bank in banks" :key="bank.id" class="flex items-center gap-2">
        <img :src="bank.logo" alt="Bank Logo" class="w-8 h-8" />
        <span>{{ bank.name }}</span>
      </div>
    </div>
  </template>
  
  <script setup>
  import { banks, savingsBanks } from "@/data/bankData";
  
  defineProps({
    type: {
      type: String,
      default: "banks", // 기본값은 일반 은행
    },
  });
  
  const bankList = type === "banks" ? banks : savingsBanks;
  </script>
  