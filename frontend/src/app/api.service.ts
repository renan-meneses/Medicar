import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http'
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class ApiService {
  baseUrl = 'http://localhost:8000/';
  httpHeader =  new HttpHeaders({'Content-Type': 'application/json'});
  constructor(private http: HttpClient){ }

  getAllMedicos() : Observable<any> {
    return this.http.get(this.baseUrl + 'medicos/', 
    {headers: this.httpHeader});
  }
}
