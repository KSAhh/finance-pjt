<!-- src/components/loan/loanpage/BankFilterCarousel.vue -->
<template>
    <div class="bank-filter-carousel">
      <div class="bank-item" v-for="bank in reactiveBanks" :key="bank.id">
        <button
          :class="['bank-button', { active: bank.active }]"
          @click="toggleBank(bank.id)"
        >
          <img :src="bank.logo" :alt="bank.name" />
          <span>{{ bank.name }}</span>
        </button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { reactive } from 'vue';
  import { defineEmits } from 'vue';
  import { banks as importedBanks } from '@/components/loan/loanpage/filterOptions.js';
  
  const emit = defineEmits(['bank-filter-changed']);
  
  // `importedBanks`는 불변 객체이므로, 각 은행에 `active` 속성을 추가하여 반응형으로 만듭니다.
  const reactiveBanks = reactive(
    importedBanks.map(bank => ({ ...bank, active: false }))
  );
  
  function toggleBank(id) {
    reactiveBanks.forEach(bank => {
      bank.active = bank.id === id;
    });
    const selectedBank = reactiveBanks.find(bank => bank.active);
    const bankId = selectedBank ? selectedBank.id : null;
    emit('bank-filter-changed', bankId);
  }
  </script>
  
  <style scoped>
  .bank-filter-carousel {
    display: flex;
    overflow-x: auto;
    padding: 10px 0;
  }
  .bank-filter-carousel::-webkit-scrollbar {
    display: none;
  }
  .bank-item {
    flex: none;
    margin-right: 10px;
  }
  .bank-button {
    display: flex;
    flex-direction: column;
    align-items: center;
    border: none;
    background: none;
    cursor: pointer;
  }
  .bank-button img {
    width: 40px;
    height: 40px;
  }
  .bank-button.active img {
    border: 2px solid #09aa5c;
    border-radius: 50%;
  }
  .bank-button span {
    margin-top: 5px;
    font-size: 12px;
  }
  </style>
  