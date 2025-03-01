import { defineStore } from "pinia";
import { BookItem } from "@/types";
import { apiUrl } from "@/services/ApiService";
import { useCategoryStore } from "@/stores/CategoryStore";

export const useBookStore = defineStore("BookStore", {
  state: () => ({
    bookList: [] as BookItem[],
  }),
  actions: {
    async fetchBooks(categoryName: string) {
      const categoryStore = useCategoryStore();

      let selectedCategoryName = categoryName;

      const selectedCategory = categoryStore.categoryList?.find(
        (category) => category.name === categoryName
      );
      if (selectedCategory) {
        selectedCategoryName = selectedCategory.name;
      }

      const url =
        apiUrl + "/books/by-category-name/" + selectedCategoryName;

      const rawBooks = await fetch(url).then((response) => response.json());

      // Convert snake_case (json) into camelCase (BookItem)
      this.bookList = rawBooks.map((book: any) => ({
        bookId: book.id,       // `id` -> `bookId`
        title: book.title,
        author: book.author,
        price: book.price,
        isPublic: book.is_public // `is_public` -> `isPublic`
      }));
    },
  },
  // getters
});
