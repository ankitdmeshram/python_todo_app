import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DataServiceService {

  constructor(
    private http: HttpClient
  ) { }

  url: string = "http://localhost:5000"

  Todos = () => {
    return this.http.get(`${this.url}/todos`)
  }

  createTodo = (data:any) => {
    return this.http.post(`${this.url}/todos`, data)
  }

  updateTodo = (data:any) => {
    return this.http.put(`${this.url}/todos/${data.id}`, data)
  }

  delete = (data:any) => {
    return this.http.delete(`${this.url}/todos/${data.id}`)
  }


}
