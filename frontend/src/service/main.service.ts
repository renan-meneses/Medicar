import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';

import { User } from '../app/components/interface/user';
import { Specialty } from '../app/components/interface/specialty';
import { Doctor } from '../app/components/interface/doctor';
import { Consultation } from '../app/components/interface/consultation'
import { Agenda } from '../app/components/interface/agenda';

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

  getSpecialties(): Observable<Specialty[]> {
    return this.http.get<Specialty[]>(`${this.url}/especialidades/`);
  }

  getDoctorsFilterSpecialties(specialtyId: number): Observable<Doctor[]> {
    return this.http.get<Doctor[]>(`${this.url}/medicos/?specialty=${specialtyId}`);
  }

  getAgendasFilterDoctors(doctorId: number): Observable<Agenda[]> {
    return this.http.get<Agenda[]>(`${this.url}/agendas/?doctor=${doctorId}`);
  }

  postConsultations(data: Consultation): Observable<Consultation> {
    return this.http.post<Consultation>(`${this.url}/consultas/`, data);
  }  

  getConsultations(): Observable<Consultation[]> {
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${localStorage.getItem('token')}`
    });
    return this.http.get<Consultation[]>(`${this.url}/consultas/`, { headers });
  }

  deleteConsultation(id: number): Observable<void> {
    return this.http.delete<void>(`${this.url}/consultas/${id}`);
  }
   
}
