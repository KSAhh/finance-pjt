<!-- src/components/loan/loanpage/BankFilterCarousel.vue -->
<template>
    <div class="bank-filter-carousel">
      <div class="bank-item" v-for="bank in reactiveBanks" :key="bank.id">
        <button
          :class="['bank-button', { active: bank.active }]"
          @click="toggleBank(bank.id)"
        >
          <img :src="bank.logoSrc" :alt="bank.name" />

          <span>{{ bank.name }}</span>
        </button>
      </div>

      
    </div>
  </template>
  
  <script setup>
  import { reactive } from 'vue';
  import { defineEmits } from 'vue';
  import { banks as importedBanks } from '@/components/loan/loanpage/filterOptions.js';
  import { useBankNameStore } from '@/stores/banknamestore';
  import { computed, ref, onMounted } from 'vue';



  // `importedBanks`는 불변 객체이므로, 각 은행에 `active` 속성을 추가하여 반응형으로 만듦
  const reactiveBanks = reactive(
    importedBanks.map(bank => ({ ...bank, active: false, logoSrc: null, }))
  )

  // 동적으로 이미지 로드
  onMounted(async () => {
    for (const bank of reactiveBanks) {
      if (typeof bank.logo === 'function') {
        const module = await bank.logo();
        bank.logoSrc = module.default; // 이미지 경로를 logoSrc에 저장
      }
    }
  });



  
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
  