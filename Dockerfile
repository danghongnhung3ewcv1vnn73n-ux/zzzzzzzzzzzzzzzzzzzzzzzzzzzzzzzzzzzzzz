# Sử dụng image Alpine mới nhất
FROM node:lts-slim

# Thiết lập thư mục làm việc bên trong container
WORKDIR /app

# COPY tất cả các file từ thư mục hiện tại của Dockerfile vào thư mục /app trong container
COPY . .

# Cấp quyền thực thi cho tất cả các file
RUN chmod +x *

# Chạy chương trình slave. Lưu ý: RUN sẽ thực thi lệnh và sau đó kết thúc.
RUN ./slave

