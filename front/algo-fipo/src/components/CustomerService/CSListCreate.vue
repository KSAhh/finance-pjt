<template>
    <div class="bg-gray-50 min-h-screen flex justify-center items-center p-6">
        <div class="w-full max-w-3xl bg-white rounded-lg shadow-lg p-8">
            <h1 class="text-2xl font-bold text-gray-800 mb-6">새 글 작성</h1>
            <form @submit.prevent="submitArticle">
                <div class="mb-4">
                    <label for="title" class="block text-sm font-medium text-gray-700 mb-1">제목</label>
                    <input
                        id="title"
                        v-model="title"
                        type="text"
                        class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
                        placeholder="제목을 입력하세요"
                        required
                    />
                </div>
                <div class="mb-6">
                    <label for="body" class="block text-sm font-medium text-gray-700 mb-1">내용</label>
                    <textarea
                        id="body"
                        v-model="body"
                        rows="6"
                        class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
                        placeholder="내용을 입력하세요"
                        required
                    ></textarea>
                </div>
                <div class="mb-4">
                    <label for="image" class="block text-sm font-medium text-gray-700 mb-1">이미지</label>
                    <input
                        id="image"
                        type="file"
                        @change="onFileChange"
                        class="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
                    />
                </div>
                <div class="mb-4">
                    <label class="inline-flex items-center">
                        <input
                            type="checkbox"
                            v-model="isPrivate"
                            class="form-checkbox text-blue-600 border-gray-300 rounded"
                        />
                        <span class="ml-2 text-sm text-gray-700">비공개</span>
                    </label>
                </div>
                <div class="flex justify-end">
                    <button
                        type="submit"
                        class="bg-blue-500 text-white px-4 py-2 rounded-lg shadow-md hover:bg-blue-600 transition"
                    >
                        작성 완료
                    </button>
                </div>
            </form>
        </div>
    </div>
</template>
<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useCsStore } from '@/stores/csStore';

const router = useRouter();
const store = useCsStore();

// 입력 필드 바인딩
const title = ref('')
const body = ref('')
const isPrivate = ref(false); // 공개 여부
const image = ref(null) // 이미지 파일

// 이미지 파일 처리
const onFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
        image.value = file
    }
}

// 글 작성 API 호출
const submitArticle = async () => {
    if (!title.value || !body.value) {
        alert('제목과 내용을 입력해주세요.');
        return;
    }

    try {
        await store.createArticle({
            title: title.value,
            article_body: body.value,
            image: image.value,
            is_private: isPrivate.value,
        });
        router.push('/cs'); // 작성 완료 후 고객센터 페이지로 이동
    } catch (error) {
        console.error('글 작성 실패:', error);
        alert('글 작성 중 오류가 발생했습니다.');
    }
};
</script>
