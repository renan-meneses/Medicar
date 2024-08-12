import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { MainService } from '../../../../service/main.service';

@Component({
  selector: 'app-consultation-create',
  templateUrl: './consultation-create.component.html',
  styleUrls: ['./consultation-create.component.css']
})
export class ConsultationCreateComponent implements OnInit {
  consultations = [];
  specialties = [];
  doctors = [];
  agendas = [];
  times = [];

  consultation!: object;
  specialtie!: object;
  doctor!: object;
  agenda!: object;
  time!: object;

  createForm: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
    private mainService: MainService,
    private router: Router
  ) {
    this.createForm = this.formBuilder.group({
      'specialty': [null, [Validators.required]],
      'doctor': [null, [Validators.required]],
      'agenda': [null, [Validators.required]],
      'time': [null, [Validators.required]]
    });
  }

  ngOnInit() {
    this.mainService.getSpecialties().subscribe(data => {
      this.specialties = data;
    })
  }

  onChangeSpecialty(id: string) {
    this.mainService.getDoctorsFilterSpecialties(parseInt(id)).subscribe(data => {
      this.doctors = data;
    })
  }

  onChangeDoctor(id: string) {
    this.mainService.getAgendasFilterDoctors(parseInt(id)).subscribe(data => {
      this.agendas = data;
    })
  }

  onChangeAgenda(id: string) {
    const selectedAgenda = this.agendas.find(a => a.id === parseInt(id));
    if (selectedAgenda) {
      this.agenda = selectedAgenda;
      this.times = [...selectedAgenda.schedule]; // Acessa o campo `schedule` diretamente
    } else {
      console.error(`Agenda with id ${id} not found`);
      this.times = [];
    }
  }
  

  onSubmit() {
    let data = {
      agenda_id: parseInt(this.createForm.get('agenda').value),
      hourly: this.createForm.get('time').value
    }
    this.mainService.postConsultations(data).subscribe(() => {
      this.router.navigate(['home'])
    }, (err) => {
      console.error(err);
    });
  }
}
