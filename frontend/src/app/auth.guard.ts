import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';
import { MainService } from '../service/main.service';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {

  constructor(
    public authService: MainService,
    private router: Router
  ) {}

  canActivate(): boolean {
    if (!this.checkToken()) {
      this.router.navigate(["login"]);
      return false;
    }
    return true;
  }

  public checkToken(): boolean {
    return !!localStorage.getItem("token");
  }
}
