"""Help message for CLI arguments."""

HELP = {
    "config": (
        """
1) Path to a HuggingFace model directory that contains a `config.json` or
2) Path to `config.json` in HuggingFace format, or
3) The name of a pre-defined model architecture.

A `config.json` file in HuggingFace format defines the model architecture, including the vocabulary
size, the number of layers, the hidden size, number of attention heads, etc.
Example: https://huggingface.co/codellama/CodeLlama-7b-hf/blob/main/config.json.

A HuggingFace directory often contains a `config.json` which defines the model architecture,
the non-quantized model weights in PyTorch or SafeTensor format, tokenizer configurations,
as well as an optional `generation_config.json` provides additional default configuration for
text generation.
Example: https://huggingface.co/codellama/CodeLlama-7b-hf/tree/main.
"""
    ).strip(),
    "quantization": """
The quantization mode we use to compile. If unprovided, will infer from `model`.
""".strip(),
    "model": """
A path to ``mlc-chat-config.json``, or an MLC model directory that contains `mlc-chat-config.json`.
It can also be a link to a HF repository pointing to an MLC compiled model.
""".strip(),
    "model_lib_path": """
The full path to the model library file to use (e.g. a ``.so`` file). If unspecified, we will use
the provided ``model`` to search over possible paths. It the model lib path is not found, it will be 
compiled in a JIT manner.
""".strip(),
    "model_type": """
Model architecture such as "llama". If not set, it is inferred from `mlc-chat-config.json`.
""".strip(),
    "device_compile": """
The GPU device to compile the model to. If not set, it is inferred from GPUs available locally.
""".strip(),
    "device_quantize": """
The device used to do quantization such as "cuda" or "cuda:0". Will detect from local available GPUs
if not specified.
""".strip(),
    "device_deploy": """
The device used to deploy the model such as "cuda" or "cuda:0". Will detect from local
available GPUs if not specified.
""".strip(),
    "host": """
The host LLVM triple to compile the model to. If not set, it is inferred from the local CPU and OS.
Examples of the LLVM triple:
1) iPhones: arm64-apple-ios;
2) ARM64 Android phones: aarch64-linux-android;
3) WebAssembly: wasm32-unknown-unknown-wasm;
4) Windows: x86_64-pc-windows-msvc;
5) ARM macOS: arm64-apple-darwin.
""".strip(),
    "opt": """
Optimization flags. MLC LLM maintains a predefined set of optimization flags,
denoted as O0, O1, O2, O3, where O0 means no optimization, O2 means majority of them,
and O3 represents extreme optimization that could potentially break the system.
Meanwhile, optimization flags could be explicitly specified via details knobs, e.g.
--opt="cublas_gemm=1;cudagraph=0".
""".strip(),
    "system_lib_prefix": """
Adding a prefix to all symbols exported. Similar to "objcopy --prefix-symbols".
This is useful when compiling multiple models into a single library to avoid symbol
conflicts. Different from objcopy, this takes no effect for shared library.
""".strip(),
    "context_window_size": """
Option to provide the maximum sequence length supported by the model.
This is usually explicitly shown as context length or context window in the model card.
If this option is not set explicitly, by default,
it will be determined by `context_window_size` or `max_position_embeddings` in `config.json`,
and the latter is usually inaccurate for some models.
""".strip(),
    "output_compile": """
The path to the output file. The suffix determines if the output file is a shared library or
objects. Available suffixes:
1) Linux: .so (shared), .tar (objects);
2) macOS: .dylib (shared), .tar (objects);
3) Windows: .dll (shared), .tar (objects);
4) Android, iOS: .tar (objects);
5) Web: .wasm (web assembly).
""".strip(),
    "source": """
The path to original model weight, infer from `config` if missing.
""".strip(),
    "source_format": """
The format of source model weight, infer from `config` if missing.
""".strip(),
    "output_quantize": """
The output directory to save the quantized model weight. Will create `params_shard_*.bin` and
`ndarray-cache.json` in this directory.
""".strip(),
    "conv_template": """
Conversation template. It depends on how the model is tuned. Use "LM" for vanilla base model
""".strip(),
    "output_gen_mlc_chat_config": """
The output directory for generated configurations, including `mlc-chat-config.json` and tokenizer
configuration.
""".strip(),
    "sliding_window_size": """
(Experimental) The sliding window size in sliding window attention (SWA).
This optional field overrides the `sliding_window_size` in config.json for
those models that use SWA. Currently only useful when compiling Mistral.
This flag subjects to future refactoring.
""".strip(),
    "prefill_chunk_size": """
(Experimental) The chunk size during prefilling. By default,
the chunk size is the same as sliding window or max sequence length.
This flag subjects to future refactoring.
""".strip(),
    "attention_sink_size": """
(Experimental) The number of stored sinks. Only supported on Mistral yet. By default,
the number of sinks is 4. This flag subjects to future refactoring.
""".strip(),
    "max_batch_size": """
The maximum allowed batch size set for the KV cache to concurrently support.
""".strip(),
    """tensor_parallel_shards""": """
Number of shards to split the model into in tensor parallelism multi-gpu inference.
""".strip(),
    "overrides": """
Model configuration override. Configurations to override `mlc-chat-config.json`. Supports
`context_window_size`, `prefill_chunk_size`, `sliding_window_size`, `attention_sink_size`,
`max_batch_size` and `tensor_parallel_shards`. Meanwhile, model config could be explicitly
specified via details knobs, e.g. --overrides "context_window_size=1024;prefill_chunk_size=128".
""".strip(),
    "chatconfig_overrides": """
Chat configuration override. Configurations to override ChatConfig. Supports `conv_template`,
`context_window_size`, `prefill_chunk_size`, `sliding_window_size`, `attention_sink_size`,
`max_batch_size` and `tensor_parallel_shards`. Meanwhile, model chat could be explicitly
specified via details knobs, e.g. --overrides "context_window_size=1024;prefill_chunk_size=128".
""".strip(),
    "debug_dump": """
Specifies the directory where the compiler will store its IRs for debugging purposes
during various phases of compilation. By default, this is set to `None`, indicating
that debug dumping is disabled.
""".strip(),
    "prompt": """
The prompt of the text generation.
""".strip(),
    "generate_length": """
The target length of the text generation.
""".strip(),
    "max_total_sequence_length_serve": """
The KV cache total token capacity, i.e., the maximum total number of tokens that
the KV cache support. This decides the GPU memory size that the KV cache consumes.
If not specified, system will automatically estimate the maximum capacity based
on the vRAM size on GPU.
""".strip(),
    "prefill_chunk_size_serve": """
The maximum number of tokens the model passes for prefill each time.
It should not exceed the prefill chunk size in model config.
If not specified, this defaults to the prefill chunk size in model config.
""".strip(),
    "max_history_size_serve": """
The max history length for rolling back.
If not specified, the default is 1.
""".strip(),
    "enable_tracing_serve": """
Enable Chrome Tracing for the server.
After enabling, you can send POST request to the "debug/dump_event_trace" entrypoint
to get the Chrome Trace. For example,
"curl -X POST http://127.0.0.1:8000/debug/dump_event_trace -H "Content-Type: application/json" -d '{"model": "dist/llama"}'"
""".strip(),
}
