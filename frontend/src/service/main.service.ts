import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';

import { User } from '../app/components/interface/user';
import { Specialty } from '../app/components/interface/specialty';
import { Doctor } from '../app/components/interface/doctor';
import { Consultation } from '../app/components/interface/consultation'


@Injectable({
  providedIn: 'root'
})
export class MainService {

  constructor(private http: HttpClient, private router : Router) { }

  url = 'http://localhost:8000'

  // authentications
  register(data: User): Observable<User> {
    return this.http.post<User>(`${this.url}/users/`, data);
  }

  login(credentials: { username: string, password: string }): Observable<{ token: string, name: string }> {
    return this.http.post<{ token: string, name: string }>(`${this.url}/api/signin/`, credentials);
  }
  

  logout() {
    localStorage.removeItem("token");
    this.router.navigate(["login"]);
  }

  // specialties
  getSpecialties(): Observable<Specialty[]> {
    return this.http.get<Specialty[]>(`${this.url}/especialidades/`);
  }

  // doctors
  getDoctorsFilterSpecialties(specialtyId: number): Observable<Doctor[]> {
    return this.http.get<Doctor[]>(`${this.url}/medicos/?specialty=${specialtyId}`);
  }

  // agendas
  getAgendasFilterDoctors(doctorId: number): Observable<object[]> {
    return this.http.get<object[]>(`${this.url}/agendas/?doctor=${doctorId}`);
  }

  // consultations
  postConsultations(data: object): Observable<object> {
    return this.http.post<object>(`${this.url}/consultas/`, data);
  }

  getConsultations(): Observable<Consultation[]> {
    return this.http.get<Consultation[]>(`${this.url}/consultas/`);
  }

  deleteConsultation(id: number) {
    return this.http.delete<{}>(`${this.url}/consultas/${id}`);
  }  
}
