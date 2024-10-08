import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { MainService } from '../../../../service/main.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  loginForm!: FormGroup;
  submitted = false;

  constructor(
    private formBuilder: FormBuilder, 
    private mainService: MainService,
    private router: Router
  ) { }

  ngOnInit() {
    this.loginForm = this.formBuilder.group({
      'username': ['', [Validators.required]],
      'password': ['', [Validators.required, Validators.minLength(6)]],
    });
  }

  onSubmit() {
    let credentials = this.loginForm.value;
    
    this.mainService.login(credentials).subscribe((res: LoginResponse) => {
      if (res.token) {
        localStorage.setItem("token", res.token);
        localStorage.setItem("name", res.name);
        this.router.navigate(['home']);
      }
    }, (err) => {
      console.error(err);
    });
  }
  
}
