import { Component } from '@angular/core';
import { ApiService } from './api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'frontend';

  medicos = [
    {nome: "Medico 1", especiadalidade:"Pediatria", crm:"000"},
    {nome: "Medico 1", especiadalidade:"Pediatria", crm:"000"},
    {nome: "Medico 1", especiadalidade:"Pediatria", crm:"000"},
    {nome: "Medico 1", especiadalidade:"Pediatria", crm:"000"},
    {nome: "Medico 1", especiadalidade:"Pediatria", crm:"000"},
    {nome: "Medico 1", especiadalidade:"Pediatria", crm:"000"},
    {nome: "Medico 1", especiadalidade:"Pediatria", crm:"000"},
    {nome: "Medico 1", especiadalidade:"Pediatria", crm:"000"},

  ];

  constructor(private api:ApiService)
  {
    this.getMedicos();
  }
  getMedicos = () => {
    this.api.getAllMedicos().subscribe(
      data => {
        this.medicos = data
      }, 
      error => 
      console.log("Aconteceu um erro", error)
    )
  }


}
