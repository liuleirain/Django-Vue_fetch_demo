<template>
  <div id="app">
    <form @submit.prevent="submitForm">
      <div class="row form-group">
        <input
          type="text"
          class="form-control mx-2 col-3"
          placeholder="Name"
          v-model="student.name"
        />
        <input
          type="text"
          class="form-control mx-2 col-3"
          placeholder="Course"
          v-model="student.course"
        />
        <input
          type="text"
          class="form-control mx-2 col-3"
          placeholder="Rating"
          v-model="student.rating"
        />
        <button class="btn btn-success">Submit</button>
      </div>
    </form>

    <table class="table">
      <thead>
        <th>Name</th>
        <th>Course</th>
        <th>Rating</th>
      </thead>
      <tbody>
        <tr v-for="student in students" :key="student.id" @dblclick="$data.student = student">
          <td>{{ student.name }}</td>
          <td>{{ student.course }}</td>
          <td>{{ student.rating }}</td>
          <td>
            <button class="btn btn-outline-danger mx-1 btn-sm" @click="deleteStudent(student)">X</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      student: {
        name: "",
        course: "",
        rating: ""
      },
      students: []
    };
  },
  components: {},
  async created() {
    await this.getStudents();
  },
  methods: {
    submitForm() {
      if (this.student.id === undefined) {
        this.createStudent();
      } else {
        this.editStudent();
      }
    },
    async getStudents() {
      var response = await fetch("http://localhost:8000/api/students/");
      this.students = await response.json();
    },
    async createStudent() {
      await this.getStudents();
      await fetch("http://localhost:8000/api/students/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(this.student)
      });
      await this.getStudents();
    },
    async editStudent() {
      await this.getStudents();
      await fetch(`http://localhost:8000/api/students/${this.student.id}/`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(this.student)
      });
      await this.getStudents();
      this.student = {};
    },
    async deleteStudent(student) {
      await this.getStudents();
      await fetch(`http://localhost:8000/api/students/${student.id}/`, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(this.student)
      });
      await this.getStudents();
      this.student = {};
    }
  }
};
</script>

<style>
</style>
