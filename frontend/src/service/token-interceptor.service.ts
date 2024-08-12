import { Injectable } from '@angular/core';
import { HttpInterceptor, HttpRequest, HttpHandler, HttpEvent } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TokenInterceptorService implements HttpInterceptor {

  constructor() { }

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    const token = this.getToken();

    if (token) {
      const tokenizedReq = req.clone({
        setHeaders: {
          'Content-Type': 'application/json',
          'Authorization': `Token ${token}`
        }
      });
      return next.handle(tokenizedReq);
    } else {
      return next.handle(req);
    }
  }

  private getToken(): string | null {
    return localStorage.getItem("token");
  }
}
