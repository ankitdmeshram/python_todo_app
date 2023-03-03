import { Component } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { ToastrService } from 'ngx-toastr';
import { DataServiceService } from './service/data-service.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'frontend';

  constructor(
    private data: DataServiceService,
    private toastr: ToastrService,
  ) {
    this.selectTodos();
  }

  todoForm = new FormGroup({
    title: new FormControl(''),
    id: new FormControl(''),
    completed: new FormControl('')
  })


  todos:any = []

  selectTodos = () => {
    this.data.Todos().subscribe((res:any) => {
      this.todos = res;
      console.log(this.todos)
    })
  }

  createTodo = () => {
    this.data.createTodo(this.todoForm.value)
    .subscribe((res:any) => {
      console.log(res)
      this.todos.push(res)
      this.todoForm.reset()
      this.toastr.success("Todo created sucessfully")
    })

  }

  editTodo = (data: any, i:number) => {
    this.todoForm.setValue(data);
    let title = prompt("Enter Title", data.title)
    if(title) {
      this.data.updateTodo({"title": title, "id": data.id, "completed": "false"}).subscribe((res) => {
        this.todos[i].title = title;
        this.todoForm.reset()
        this.toastr.success("Todo updated sucessfully")

      })
    }
  }

  isComplete = (data:any, i:number) => {

    if(data.completed == 0)
    {
      data.completed = 1;
    } else {
      data.completed = 0;
    }

    this.data.updateTodo({"title": data.title, "id": data.id, "completed": data.completed}).subscribe((res) => {
      this.todos[i].completed = data.completed;
      this.toastr.success("Todo updated sucessfully")

    })
  }

  deleteTodo = (data: any, i:number) => {

    if(confirm(`Are you sure you want to delete ${data.title}`))
    {
      this.data.delete(data).subscribe((res) => {
        console.log("Delete Succesfully")
        this.todos.splice(i, 1)
        this.toastr.success("Todo deleted sucessfully")

      })

    }
  }

}
